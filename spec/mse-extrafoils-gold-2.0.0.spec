Name: mse-extrafoils-gold
Version: 2.0.0
Release: 1%{?dist}
Summary: Various extra foils from The Foil and Overlay Thread. This one is the ghost foil gradient .
License: GPL
URL: http://mtg.pifro.com/viewtopic.php?f=19&t=704
Source0: magic-overlay-foil-gold.mse-installer::http://mtg.pifro.com/download/file.php?id=1659
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: magicseteditor
%description Various extra foils from The Foil and Overlay Thread. This one is the ghost foil gradient .

%prep
%setup -qn %_builddir/mse-extrafoils-gold-2.0.0 -c %_builddir/mse-extrafoils-gold-2.0.0

%build

    cd %_builddir;
    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    bsdtar -xf magic-overlay-foil-gold.mse-installer;
    chmod -x ./*.mse-include/*;
    cp -r ./*.mse-include %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-1
- Converted PKGBUILD to spec
