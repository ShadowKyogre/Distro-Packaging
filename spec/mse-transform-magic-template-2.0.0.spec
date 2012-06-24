Name: mse-transform-magic-template
Version: 2.0.0
Release: 2%{?dist}
Summary: Template for the newly release transformable cards
License: GPL
URL: http://mtg.pifro.com/viewtopic.php?f=26&t=1455
Source0: magic-transform.mse-installer::http://mtg.pifro.com/download/file.php?id=2871
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: mse-mtg
%description Template for the newly release transformable cards

%prep
%setup -qn %_builddir/mse-transform-magic-template-2.0.0 -c %_builddir/mse-transform-magic-template-2.0.0

%build

    cd %_builddir;
    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    bsdtar -xf magic-transform.mse-installer;
    chmod -x ./*.mse-style/*;
    cp -r ./*.mse-style %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-2
- Converted PKGBUILD to spec
