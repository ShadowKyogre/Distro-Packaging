Name: mse-extracolors-magic-template
Version: 2.0.0
Release: 5%{?dist}
Summary: The standard Magic: the Gathering cards with more colors
License: GPL
URL: http://magicseteditor.sourceforge.net/additional-templates
Source0: magic-mana-small-and-large-extra.mse-installer::http://mtg.pifro.com/download/file.php?id=2851
Source1: magic-new-extra.mse-installer::http://mtg.pifro.com/download/file.php?id=2608
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: mse-mtg
%description The standard Magic: the Gathering cards with more colors

%prep
%setup -qn %_builddir/mse-extracolors-magic-template-2.0.0 -c %_builddir/mse-extracolors-magic-template-2.0.0

%build

    cd %_builddir;
    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    bsdtar -xf magic-new-extra.mse-installer;
    bsdtar -xf magic-mana-small-and-large-extra.mse-installer;
    sed -e 's|emblem|watermark|g' -i ./*.mse-style/style;
    chmod -x ./*.mse-s{tyle,ymbol-font}/*;
    chmod -x ./magic-watermarks-extra.mse-include/*;
    cp -r ./magic-watermarks-extra.mse-include %_buildrootdir/usr/share/magicseteditor/data;
    cp -r ./*.mse-s{tyle,ymbol-font} %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-5
- Converted PKGBUILD to spec
