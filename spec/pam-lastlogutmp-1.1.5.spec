Name: pam-lastlogutmp
Version: 1.1.5
Release: 4%{?dist}
Summary: PAM (Pluggable Authentication Modules) library (patched to provide utmp logging for lastlog)
License: GPL2
URL: http://www.kernel.org/pub/linux/libs/pam/
Source0: https://fedorahosted.org/releases/l/i/linux-pam/Linux-PAM-1.1.5.tar.bz2
Source1: ftp://ftp.suse.com/pub/people/kukuk/pam/pam_unix2/pam_unix2-2.6.tar.bz2
Source2: lastlog_write_to_utmp.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: flex w3m docbook-xml>=4.4 docbook-xsl
Requires: glibc db cracklib libtirpc pambase
%description PAM (Pluggable Authentication Modules) library (patched to provide utmp logging for lastlog)

%prep
%setup -qn %_builddir/pam-lastlogutmp-1.1.5 -c %_builddir/pam-lastlogutmp-1.1.5

%build

    cd %_builddir/Linux-PAM-$pkgver;
    patch -Np1 -i "%_builddir/lastlog_write_to_utmp.patch";
    ./configure --libdir=/usr/lib;
    make;
    cd %_builddir/pam_unix2-2.6;
    ./configure --libdir=/usr/lib;
    make

%install

    cd %_builddir/Linux-PAM-$pkgver;
    make DESTDIR=%_buildrootdir install;
    cd %_builddir/pam_unix2-2.6;
    make DESTDIR=%_buildrootdir install;
    sed -i 's|# End of file||' %_buildrootdir/etc/security/limits.conf;
    cat >> %_buildrootdir/etc/security/limits.conf  <<_EOT
*               -       rtprio          0
*               -       nice            0
@audio          -       rtprio          65
@audio          -       nice           -10
@audio          -       memlock         40000
_EOT

    cd %_buildrootdir/usr/lib/security;
    ln -s pam_unix.so pam_unix_acct.so;
    ln -s pam_unix.so pam_unix_auth.so;
    ln -s pam_unix.so pam_unix_passwd.so;
    ln -s pam_unix.so pam_unix_session.so;
    chmod +s %_buildrootdir/sbin/unix_chkpwd

%files
%defattr(-,root,root,-)
/

%posttrans

    /sbin/ldconfig -r .;
    echo "Please add noutmp to your /etc/pam.d/login for the lastlog entry";
    echo "Otherwise, it'll log it twice"

%post

    posttrans $1

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 1.1.5-4
- Converted PKGBUILD to spec
