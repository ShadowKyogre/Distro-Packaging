Name: mse-poker-template
Version: 2.0.0
Release: 1%{?dist}
Summary: Poker card template for Magic Set Editor
License: GPL
URL: http://magicseteditor.sourceforge.net
Source0: poker.mse-installer::http://mtg.pifro.com/download/file.php?id=2412&sid=c91b0e6fb4bcfca1b75d552e0fad5e1c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: magicseteditor
%description Poker card template for Magic Set Editor

%prep
%setup -qn %_builddir/mse-poker-template-2.0.0 -c %_builddir/mse-poker-template-2.0.0

%build

    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    bsdtar -xf poker.mse-installer;
    chmod -x ./*.mse-{style,game,symbol-font}/*;
    cp -r ./*.mse-{style,game,symbol-font} %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-1
- Converted PKGBUILD to spec
