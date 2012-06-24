Name: mse-cbg-ygo-template
Version: 2.0.0
Release: 2%{?dist}
Summary: A more space-efficient and fancy template for the YuGiOh game.
License: GPL
URL: http://magicseteditor.sourceforge.net
Source0: yugioh-cbg.mse-installer::http://mtg.pifro.com/download/file.php?id=2481&sid=57d0b13af8cb7448a11b1b9c747b85c1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: mse-ygo ttf-lightfoot
%description A more space-efficient and fancy template for the YuGiOh game.

%prep
%setup -qn %_builddir/mse-cbg-ygo-template-2.0.0 -c %_builddir/mse-cbg-ygo-template-2.0.0

%build

    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    bsdtar -xf yugioh-cbg.mse-installer;
    chmod -x ./*.mse-style/*;
    cp -r ./*.mse-style %_buildrootdir/usr/share/magicseteditor/data;
    cp ./xyz-card.png %_buildrootdir/usr/share/magicseteditor/data/yugioh-cbg.mse-style

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-2
- Converted PKGBUILD to spec
