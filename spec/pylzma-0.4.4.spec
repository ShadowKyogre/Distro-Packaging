Name: pylzma
Version: 0.4.4
Release: 1%{?dist}
Summary: Platform independent python bindings for the LZMA compression library
License: LGPL
URL: http://www.joachim-bauch.de/projects/python/pylzma
Source0: http://pypi.python.org/packages/source/p/pylzma/pylzma-0.4.4.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: python2 libstdc++5
%description Platform independent python bindings for the LZMA compression library

%prep
%setup -qn %_builddir/pylzma-0.4.4 -c %_builddir/pylzma-0.4.4

%build

    cd $startdir/src/$pkgname-$pkgver;
    python2 setup.py install --root=$startdir/pkg

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 0.4.4-1
- Converted PKGBUILD to spec
