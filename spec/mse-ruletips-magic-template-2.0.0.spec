Name: mse-ruletips-magic-template
Version: 2.0.0
Release: 2%{?dist}
Summary: Magic: the Gathering tip card template
License: GPL
URL: http://magicseteditor.sourceforge.net/additional-templates
Source0: rulestip.mse-installer::http://mtg.pifro.com/download/file.php?id=891
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: mse-mtg
%description Magic: the Gathering tip card template

%prep
%setup -qn %_builddir/mse-ruletips-magic-template-2.0.0 -c %_builddir/mse-ruletips-magic-template-2.0.0

%build

    cd %_builddir;
    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    bsdtar -xf rulestip.mse-installer;
    cp -r ./*.mse-style %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-2
- Converted PKGBUILD to spec
