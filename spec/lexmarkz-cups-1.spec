Name: lexmarkz-cups
Version: 1
Release: 8%{?dist}
Summary: Lexmark Z35, Z55, Z65, Z600 and Z700 Printer Drivers for CUPS
License: custom
URL: http://www.lexmark.com/
Source0: http://webjdm.free.fr/archlinux/lexmarkz-cups/lexmarkz-cups-RPM.tar.gz
Source1: lexmark-eula.txt
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: rpmunpack cpio gzip bash
Requires: cups gcc-libs gnutls libstdc++5 sqlite3
%description Lexmark Z35, Z55, Z65, Z600 and Z700 Printer Drivers for CUPS

%prep
%setup -qn %_builddir/lexmarkz-cups-1 -c %_builddir/lexmarkz-cups-1

%build

    cd ${startdir}/src;
    install -D -m644 lexmark-eula.txt ${startdir}/pkg/usr/share/licenses/${pkgname}/LICENSE || return 1;
    cd ${startdir}/pkg;
    mkdir -p usr/lib/cups/backend;
    mkdir -p usr/lib/cups/filter;
    mkdir -p usr/share/cups/model;
    mkdir -p usr/include/lexmark;
    cd ${startdir}/src;
    rpmunpack z35llpddk-2.0-2.i386.rpm || return 1;
    rpmunpack lexmarkz35-CUPS-2.0-1.i386.rpm || return 1;
    gzip -d lexmarkz35-CUPS-2.0-1.cpio.gz || return 1;
    gzip -d z35llpddk-2.0-2.cpio.gz || return 1;
    cd ${startdir}/pkg;
    mkdir -p usr/local/z35llpddk/utility;
    cpio -i < ${startdir}/src/lexmarkz35-CUPS-2.0-1.cpio || return 1;
    cpio -i < ${startdir}/src/z35llpddk-2.0-2.cpio || return 1;
    rm -f usr/include/lexmark/*;
    rm -f usr/lib/liblexprint*;
    cd ${startdir}/src;
    rpmunpack z55llpddk-2.0-2.i386.rpm || return 1;
    rpmunpack lexmarkz55-CUPS-1.0-1.i386.rpm || return 1;
    gzip -d lexmarkz55-CUPS-1.0-1.cpio.gz || return 1;
    gzip -d z55llpddk-2.0-2.cpio.gz || return 1;
    cd ${startdir}/pkg;
    mkdir -p usr/local/z55llpddk/utility;
    cpio -i < ${startdir}/src/lexmarkz55-CUPS-1.0-1.cpio || return 1;
    cpio -i < ${startdir}/src/z55llpddk-2.0-2.cpio || return 1;
    rm -f usr/include/lexmark/*;
    rm -f usr/lib/liblexprint*;
    cd ${startdir}/src;
    rpmunpack z65llpddk-2.0-2.i386.rpm || return 1;
    rpmunpack lexmarkz65-CUPS-1.0-1.i386.rpm || return 1;
    gzip -d lexmarkz65-CUPS-1.0-1.cpio.gz || return 1;
    gzip -d z65llpddk-2.0-2.cpio.gz || return 1;
    cd ${startdir}/pkg;
    mkdir -p usr/local/z65llpddk/utility;
    cpio -i < ${startdir}/src/lexmarkz65-CUPS-1.0-1.cpio || return 1;
    cpio -i < ${startdir}/src/z65llpddk-2.0-2.cpio || return 1;
    rm -f usr/include/lexmark/*;
    rm -f usr/lib/liblexprint*;
    cd ${startdir}/src;
    rpmunpack z700llpddk-2.0-1.i386.rpm || return 1;
    rpmunpack lexmark-z700-cups-driver-1.1.1-1.i586.rpm || return 1;
    gzip -d z700llpddk-2.0-1.cpio.gz || return 1;
    gzip -d lexmark-z700-cups-driver-1.1.1-1.cpio.gz || return 1;
    cd ${startdir}/pkg;
    mkdir -p usr/local/z700llpddk/utility;
    cpio -i < ${startdir}/src/z700llpddk-2.0-1.cpio || return 1;
    cpio -i < ${startdir}/src/lexmark-z700-cups-driver-1.1.1-1.cpio || return 1;
    rm -f usr/include/lexmark/*;
    rm -f usr/lib/liblexprint*;
    cd ${startdir}/src;
    rpmunpack z600llpddk-2.0-1.i386.rpm || return 1;
    rpmunpack z600cups-1.0-1.i386.rpm || return 1;
    gzip -d z600cups-1.0-1.cpio.gz || return 1;
    gzip -d z600llpddk-2.0-1.cpio.gz || return 1;
    cd ${startdir}/pkg;
    mkdir -p usr/local/z600llpddk/utility;
    cpio -i < $startdir/src/z600cups-1.0-1.cpio || return 1;
    cpio -i < $startdir/src/z600llpddk-2.0-1.cpio || return 1;
    cd ${startdir}/pkg;
    rm -Rf usr/local/z700cups;
    rm -Rf usr/include;
    rm -Rf usr/lib/cups/backend;
    find . -name '*.la' -exec rm {} \;;
    if [ "$CARCH" = "x86_64" ]; then
        mkdir -p opt/lib32/usr/lib;
        cp usr/lib/*.* opt/lib32/usr/lib;
    fi

%files
%defattr(-,root,root,-)
/

%posttrans

    cat  <<_EOF
==> Z35 driver for:
 -> Lexmark Z23/Z25/Z33/Z33/Z35
==> Z55 driver for:
 -> Lexmark Z55/Z513/Z515/Z517/X5150
==> Z65 driver :
 -> Lexmark Z65
==> Z700 driver for:
 -> Lexmark Z700/Z703/Z705/Z707/Z708 and P706
 -> Lexmark P3150/P3120
==> Z600 driver for:
 -> Lexmark Z601/Z602/Z603/Z604/Z605/Z611/Z612/Z613/Z614/Z615/Z617
 -> Lexmark X1100/X1110/X1130/X1140/X1150/X1170/X1185/X1190/X1195
 -> Lexmark X1240/X1250/X1270/X1290
 -> Dell A920, Dell Photo 720
==> Open up your browser and go to: http://localhost:631 
_EOF

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 1-8
- Converted PKGBUILD to spec
