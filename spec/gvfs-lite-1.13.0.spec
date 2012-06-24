Name: gvfs-lite
Version: 1.13.0
Release: 1%{?dist}
Summary: Userspace virtual filesystem implemented as a pluggable module for gio
License: LGPL
URL: http://www.gnome.org
Source0: http://ftp.gnome.org/pub/gnome/sources/gvfs/1.13/gvfs-1.13.0.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: fuse>=2.8.4 bluez>=4.77 smbclient>=3.5.5 pkgconfig intltool
Requires: 
%description Userspace virtual filesystem implemented as a pluggable module for gio

%prep
%setup -qn %_builddir/gvfs-lite-1.13.0 -c %_builddir/gvfs-lite-1.13.0

%build

    cd "%_builddir/${_getthis}-${pkgver}";
    ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --disable-static --libexecdir=/usr/lib/gvfs --with-bash-completion-dir=/etc/bash_completion.d;
    make

%install

    cd "%_builddir/${_getthis}-${pkgver}";
    sed -e 's/^am__append_3/#am__append_3/' -e 's/^am__append_4/#am__append_4/' -i monitor/Makefile;
    make DESTDIR="%_buildrootdir" install;
    cd "%_buildrootdir";
    rm -f usr/lib/gvfs/gvfsd-{smb,smb-browse,afc,gphoto2,obexftp};
    rm -f usr/share/gvfs/mounts/{smb,smb-browse,afc,gphoto2,obexftp}.mount

%files
%defattr(-,root,root,-)
/

%posttrans

    usr/bin/gio-querymodules usr/lib/gio/modules;
    killall -USR1 gvfsd &>/dev/null || :

%post

    posttrans

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 1.13.0-1
- Converted PKGBUILD to spec
