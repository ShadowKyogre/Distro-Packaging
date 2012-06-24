Name: mse-mtg-phyrexian
Version: 2.0.0
Release: 6%{?dist}
Summary: Magic: the Gathering templates for Magic Set Editor.
License: freeware
URL: http://magicseteditor.sourceforge.net
Source0: http://downloads.sourceforge.net/magicseteditor/mse-linux32-2011-02-05-full.tar.gz
Source1: magic-mana-small-and-large.mse-installer::http://mtg.pifro.com/download/file.php?id=2850
Source2: magic-mana-future.mse-installer::http://mtg.pifro.com/download/file.php?id=2849
Source3: magic-mana-beveled.mse-installer::http://mtg.pifro.com/download/file.php?id=2848
Source4: magic.mse-installer::http://mtg.pifro.com/download/file.php?id=2865
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: magicseteditor
%description Magic: the Gathering templates for Magic Set Editor.

%prep
%setup -qn %_builddir/mse-mtg-phyrexian-2.0.0 -c %_builddir/mse-mtg-phyrexian-2.0.0

%build

    cd %_builddir;
    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    cp -r ./magicseteditor/program/data/{magic,archenemy,planechase}* %_buildrootdir/usr/share/magicseteditor/data;
    bsdtar -xf magic-mana-small-and-large.mse-installer;
    bsdtar -xf magic-mana-future.mse-installer;
    bsdtar -xf magic-mana-beveled.mse-installer;
    bsdtar -xf magic.mse-installer;
    cp -r ./magic*.mse-{symbol-font,game} %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-6
- Converted PKGBUILD to spec
