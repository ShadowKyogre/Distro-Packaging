Name: gvfs-smb-lite
Version: 1.13.0
Release: 1%{?dist}
Summary: SMB/CIFS (Windows client) backend for gvfs
License: LGPL
URL: http://www.gnome.org
Source0: http://ftp.gnome.org/pub/gnome/sources/gvfs/1.13/gvfs-1.13.0.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: fuse>=2.8.4 bluez>=4.77 smbclient>=3.5.5 pkgconfig intltool
Requires: gvfs-lite=1.13.0 smbclient>=3.5.5 libgnome-keyring>=2.32.0
%description SMB/CIFS (Windows client) backend for gvfs

%prep
%setup -qn %_builddir/gvfs-smb-lite-1.13.0 -c %_builddir/gvfs-smb-lite-1.13.0

%build

    cd "%_builddir/${_getthis}-${pkgver}";
    ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --disable-static --libexecdir=/usr/lib/gvfs --with-bash-completion-dir=/etc/bash_completion.d;
    make

%install

    cd "%_builddir/${_getthis}-${pkgver}/daemon";
    install -m755 -d "%_buildrootdir/usr/lib/gvfs";
    install -m755 -d "%_buildrootdir/usr/share/gvfs/mounts";
    install -m755 .libs/gvfsd-smb{,-browse} "%_buildrootdir/usr/lib/gvfs/";
    install -m644 smb{,-browse}.mount "%_buildrootdir/usr/share/gvfs/mounts/"

%files
%defattr(-,root,root,-)
/

%posttrans

    killall -USR1 gvfsd &>/dev/null || :

%post

    posttrans

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 1.13.0-1
- Converted PKGBUILD to spec
