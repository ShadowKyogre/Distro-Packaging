Name: mse-proplayers-magic-template
Version: 2.0.0
Release: 3%{?dist}
Summary: Style for the 2005 version of Magic: the Gathering Pro Players cards
License: GPL
URL: http://magicseteditor.sourceforge.net/additional-templates
Source0: magic-proplayers-2005.zip::http://mtg.pifro.com/download/file.php?id=1785
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: mse-mtg ttf-masterforce-solid
%description Style for the 2005 version of Magic: the Gathering Pro Players cards

%prep
%setup -qn %_builddir/mse-proplayers-magic-template-2.0.0 -c %_builddir/mse-proplayers-magic-template-2.0.0

%build

    cd %_builddir;
    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    bsdtar -xf magic-proplayers-2005.mse-installer;
    chmod -x ./*.mse-style/*;
    cp -r ./*.mse-style %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-3
- Converted PKGBUILD to spec
