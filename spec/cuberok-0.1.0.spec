Name: cuberok
Version: 0.1.0
Release: 1%{?dist}
Summary: Yet another music player based on Qt4.
License: GPL
URL: http://code.google.com/p/cuberok/
Source0: http://cuberok.googlecode.com/files/cuberok-0.1.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: make pkgconfig sed
Requires: qt gstreamer0.10-good-plugins phonon
%description Yet another music player based on Qt4.

%prep
%setup -qn %_builddir/cuberok-0.1.0 -c %_builddir/cuberok-0.1.0

%build

    cd %_builddir/$pkgname-$pkgver;
    sed -i 's/64//g' ./plugins/plugins_path-x86-64.pri;
    sed -i 's/64//g' ./plugins/plugins_path-x86_64.pri;
    sed -i 's/SUBDIRS += plugins\/player_ffmpeg//g' Cuberok.pro;
    sed -i s\|/usr/local\|%_buildrootdir/usr\| unix_build.sh;
    sed -i s/sudo// unix_build.sh;
    chmod +x ./unix_build.sh;
    ./unix_build.sh || return 1

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 0.1.0-1
- Converted PKGBUILD to spec
