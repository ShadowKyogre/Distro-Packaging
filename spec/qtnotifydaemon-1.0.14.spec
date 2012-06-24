Name: qtnotifydaemon
Version: 1.0.14
Release: 3%{?dist}
Summary: Configurable and flexible Qt notification daemon
License: GPL3
URL: http://sourceforge.net/projects/qtnotifydaemon
Source0: http://downloads.sourceforge.net/project/qtnotifydaemon/qtnotifydaemon_1.0.14.orig.tar.gz
Source1: override_icon_theme.patch
Source2: gcc4.7fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: qt
%description Configurable and flexible Qt notification daemon

%prep
%setup -qn %_builddir/qtnotifydaemon-1.0.14 -c %_builddir/qtnotifydaemon-1.0.14

%build

    cd %_builddir;
    patch -Ni %_builddir/override_icon_theme.patch;
    patch -Np1 -i %_builddir/gcc4.7fix.patch;
    qmake ${pkgname}.pro;
    make

%install

    cd %_builddir;
    install -Dm 755 ${pkgname} %_buildrootdir/usr/bin/${pkgname};
    install -Dm 644 org.freedesktop.Notifications.service %_buildrootdir/usr/share/dbus-1/services/org.freedesktop.Notifications.service;
    gzip debian/${pkgname}.1;
    install -Dm 644 debian/${pkgname}.1.gz %_buildrootdir/usr/share/man/man1/${pkgname}.1.gz

%files
%defattr(-,root,root,-)
/

%posttrans

    echo "Default config file $HOME/.config/qtnotifydaemon/qtnotifydaemon.conf will appear after first launch."

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 1.0.14-3
- Converted PKGBUILD to spec
