Name: mse-heroes-magic-template
Version: 2.0.0
Release: 2%{?dist}
Summary: Adds a new Magic: the Gathering card type: Hero
License: GPL
URL: http://magicseteditor.sourceforge.net/node/1319
Source0: magic-heroes.mse-installer::http://mtg.pifro.com/download/file.php?id=1713
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: mse-mtg
%description Adds a new Magic: the Gathering card type: Hero

%prep
%setup -qn %_builddir/mse-heroes-magic-template-2.0.0 -c %_builddir/mse-heroes-magic-template-2.0.0

%build

    cd %_builddir;
    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    bsdtar -xfmagic-heroes.mse-installer;
    cp -r ./*.mse-style %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-2
- Converted PKGBUILD to spec
