Name: metamorphose2
Version: 0.8.2
Release: 1%{?dist}
Summary: Batch Rename Utility
License: GPL
URL: http://file-folder-ren.sourceforge.net
Source0: http://downloads.sourceforge.net/file-folder-ren/metamorphose2_0.8.2.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: python2 wxpython
%description Batch Rename Utility

%prep
%setup -qn %_builddir/metamorphose2-0.8.2 -c %_builddir/metamorphose2-0.8.2

%build

    cd %_builddir/metamorphose2_$pkgver;
    sed -i -e "s|#![ ]*/usr/bin/python$|#!/usr/bin/python2|" -e "s|#![ ]*/usr/bin/env python$|#!/usr/bin/env python2|" $(find ./ -name '*.py');
    sed -i "s|exec python|exec python2|g" metamorphose2;
    install -d %_buildrootdir/usr/{bin,share/man/man1,share/pixmaps,share/applications,share/app-install/icons,share/app-install/desktop,share/locale};
    make DESTDIR=%_buildrootdir all

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 0.8.2-1
- Converted PKGBUILD to spec
