Name: pyswisseph3
Version: 1.77.00
Release: 1%{?dist}
Summary: Python extension to the Swiss Ephemeris. (Python 3 version)
License: GPL
URL: http://pyswisseph.chaosorigin.com/
Source0: http://pypi.python.org/packages/source/p/pyswisseph/pyswisseph-1.77.00-0.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: python
%description Python extension to the Swiss Ephemeris. (Python 3 version)

%prep
%setup -qn %_builddir/pyswisseph3-1.77.00 -c %_builddir/pyswisseph3-1.77.00

%build

    cd "%_builddir/${_orig}-$pkgver-0";
    python setup.py install --root=%_buildrootdir || return 1

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 1.77.00-1
- Converted PKGBUILD to spec
