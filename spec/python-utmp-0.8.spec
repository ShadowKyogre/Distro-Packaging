Name: python-utmp
Version: 0.8
Release: 1%{?dist}
Summary: Modules to access utmp from python.
License: GPL
URL: http://korpus.juls.savba.sk/~garabik/software/python-utmp/
Source0: http://korpus.juls.savba.sk/~garabik/software/python-utmp/python-utmp_0.8.tar.gz
Source1: slight_compat_fixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: python
%description Modules to access utmp from python.

%prep
%setup -qn %_builddir/python-utmp-0.8 -c %_builddir/python-utmp-0.8

%build

    cd "%_builddir/$_pkgroot-$pkgver";
    patch -Np1 -i "%_builddir/slight_compat_fixes.patch";
    PYTHONVER=3.2mu make -f Makefile.glibc

%install

    cd "%_builddir/$_pkgroot-$pkgver";
    PYTHONVER=3.2mu DESTDIR="%_buildrootdir/" make install

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 0.8-1
- Converted PKGBUILD to spec
