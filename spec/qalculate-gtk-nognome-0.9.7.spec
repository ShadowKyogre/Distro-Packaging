Name: qalculate-gtk-nognome
Version: 0.9.7
Release: 1%{?dist}
Summary: GTK+ frontend for libqalculate, without gnome dependencies
License: GPL
URL: http://qalculate.sourceforge.net/
Source0: http://downloads.sourceforge.net/sourceforge/qalculate/qalculate-gtk-0.9.7.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: perlxml rarian
Requires: libqalculate>=0.9.7 libglade cln>=1.2.0
%description GTK+ frontend for libqalculate, without gnome dependencies

%prep
%setup -qn %_builddir/qalculate-gtk-nognome-0.9.7 -c %_builddir/qalculate-gtk-nognome-0.9.7

%build

    cd "%_builddir/${_nick}-${pkgver}";
    ./configure --prefix=/usr --without-libgnome || return 1;
    make || return 1;
    make DESTDIR="%_buildrootdir" install || return 1

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 0.9.7-1
- Converted PKGBUILD to spec
