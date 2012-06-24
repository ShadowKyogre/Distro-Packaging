Name: tora
Version: 2.1.3
Release: 4%{?dist}
Summary: Toolkit for databases with support for MySQL and PostgreSQL
License: GPL
URL: http://tora.sourceforge.net
Source0: http://downloads.sourceforge.net/tora/tora-2.1.3.tar.gz
Source1: include_unistd.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: cmake
Requires: qscintilla
%description Toolkit for databases with support for MySQL and PostgreSQL

%prep
%setup -qn %_builddir/tora-2.1.3 -c %_builddir/tora-2.1.3

%build

    cd "%_builddir/${pkgname}-${pkgver}";
    patch -Np1 -i "%_builddir/include_unistd.patch";
    mkdir "%_builddir/build";
    cd "%_builddir/build";
    cmake ../${pkgname}-${pkgver} -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release;
    make

%install

    cd "%_builddir"/build;
    make DESTDIR="%_buildrootdir" install

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.1.3-4
- Converted PKGBUILD to spec
