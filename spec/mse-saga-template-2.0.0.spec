Name: mse-saga-template
Version: 2.0.0
Release: 3%{?dist}
Summary: Adds a new Magic: the Gathering card type: Saga
License: GPL
URL: http://magicseteditor.sourceforge.net/node/3425
Source0: saga.zip::http://mtg.pifro.com/download/file.php?id=2378&sid=da6ede4318306f68e2d68fc457622039
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: mse-mtg ttf-dasroy
%description Adds a new Magic: the Gathering card type: Saga

%prep
%setup -qn %_builddir/mse-saga-template-2.0.0 -c %_builddir/mse-saga-template-2.0.0

%build

    cd %_builddir;
    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    bsdtar -xf saga.mse-installer;
    sed -e 's|DasRoy Small Caps|DasRoy|g' -i ./*.mse-style/style;
    sed -e 's|language: "en_US",|language: "en_us",|g' -i ./*.mse-game/game;
    chmod -x ./*.mse-{gam,styl}e/*;
    chmod +x ./*.mse-game/stats;
    cp -r ./*.mse-{gam,styl}e %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-3
- Converted PKGBUILD to spec
