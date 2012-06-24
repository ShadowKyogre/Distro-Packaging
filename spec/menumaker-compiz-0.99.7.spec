Name: menumaker-compiz
Version: 0.99.7
Release: 8%{?dist}
Summary: Heuristics-driven menu generator for Deskmenu, FluxBox, IceWM, OpenBox, WindowMaker and XFCE. Now with Compiz, MyGTKMenu, urxvt, and roxterm support.
License: BSD
URL: http://menumaker.sourceforge.net/
Source0: http://downloads.sourceforge.net/menumaker/menumaker-0.99.7.tar.gz
Source1: menumaker.patch
Source2: Compiz.py
Source3: MyGTKMenu.py
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: python2
%description Heuristics-driven menu generator for Deskmenu, FluxBox, IceWM, OpenBox, WindowMaker and XFCE. Now with Compiz, MyGTKMenu, urxvt, and roxterm support.

%prep
%setup -qn %_builddir/menumaker-compiz-0.99.7 -c %_builddir/menumaker-compiz-0.99.7

%build

    cd %_builddir/${provides}-${pkgver};
    patch -Np1 -i ../menumaker.patch || return 1;
    cp %_builddir/Compiz.py %_builddir/${provides}-${pkgver}/MenuMaker;
    cp %_builddir/MyGTKMenu.py %_builddir/${provides}-${pkgver}/MenuMaker;
    sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python2
import sys; sys.path = ["/usr/lib/menumaker"] + sys.path|' ./mmaker;
    msg "Adjusting for python reconfig";
    ./configure --prefix=/usr --infodir=/usr/share/info --with-python=/usr/bin/python2;
    make -j1 || return 1;
    make DESTDIR=%_buildrootdir install;
    install -Dm644 COPYING %_buildrootdir/usr/share/licenses/${provides}/license;
    rm %_buildrootdir/usr/share/info/dir

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 0.99.7-8
- Converted PKGBUILD to spec
