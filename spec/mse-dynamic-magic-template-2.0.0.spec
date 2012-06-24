Name: mse-dynamic-magic-template
Version: 2.0.0
Release: 2%{?dist}
Summary: CBG's dynamic style for Magic: the Gathering
License: GPL
URL: http://mtg.pifro.com/viewtopic.php?f=19&t=1029
Source0: magic-dynamic.mse-installer::http://mtg.pifro.com/download/file.php?id=2092
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: mse-mtg
%description CBG's dynamic style for Magic: the Gathering

%prep
%setup -qn %_builddir/mse-dynamic-magic-template-2.0.0 -c %_builddir/mse-dynamic-magic-template-2.0.0

%build

    cd %_builddir;
    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    bsdtar -xf magic-dynamic.mse-installer;
    chmod -x ./*.mse-style/*;
    cp -r ./*.mse-style %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-2
- Converted PKGBUILD to spec
