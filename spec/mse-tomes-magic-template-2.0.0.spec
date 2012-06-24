Name: mse-tomes-magic-template
Version: 2.0.0
Release: 2%{?dist}
Summary: Adds a new card type: tomes
License: GPL
URL: http://magicseteditor.sourceforge.net/node/4839
Source0: magic-new-tome.mse-installer::http://mtg.pifro.com/download/file.php?id=2671
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: mse-mtg
%description Adds a new card type: tomes

%prep
%setup -qn %_builddir/mse-tomes-magic-template-2.0.0 -c %_builddir/mse-tomes-magic-template-2.0.0

%build

    cd %_builddir;
    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    bsdtar -xf magic-new-tome.mse-installer;
    chmod -x ./*.mse-style/*;
    cp -r ./*.mse-style %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-2
- Converted PKGBUILD to spec
