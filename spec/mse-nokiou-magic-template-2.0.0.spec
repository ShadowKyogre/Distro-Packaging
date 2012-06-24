Name: mse-nokiou-magic-template
Version: 2.0.0
Release: 4%{?dist}
Summary: An MSE version of Nokiou of MTG Salvation's custom style
License: GPL
URL: http://mtg.pifro.com/viewtopic.php?f=19&t=737
Source0: magic-nokiou.mse-installer::http://mtg.pifro.com/download/file.php?id=1755
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: mse-mtg
%description An MSE version of Nokiou of MTG Salvation's custom style

%prep
%setup -qn %_builddir/mse-nokiou-magic-template-2.0.0 -c %_builddir/mse-nokiou-magic-template-2.0.0

%build

    cd %_builddir;
    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    bsdtar -xf magic-nokiou.mse-installer;
    chmod -x ./*.mse-s{tyle,ymbol-font}/*;
    cp -r ./*.mse-s{tyle,ymbol-font} %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-4
- Converted PKGBUILD to spec
