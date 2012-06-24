Name: mse-tarot-template
Version: 2.0.0
Release: 2%{?dist}
Summary: Tarot template for Magic Set Editor
License: GPL
URL: http://magicseteditor.sourceforge.net
Source0: tarot.zip::http://mtg.pifro.com/download/file.php?id=1245&sid=03c3bc0ed8480793688c7f7f8b03ce50
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: magicseteditor ttf-tangiers
%description Tarot template for Magic Set Editor

%prep
%setup -qn %_builddir/mse-tarot-template-2.0.0 -c %_builddir/mse-tarot-template-2.0.0

%build

    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    bsdtar -xf tarot.mse-installer;
    sed -e 's|name: Algerian|name: Tangiers|g' -i ./*.mse-style/style;
    chmod -x ./*.mse-{style,game}/*;
    cp -r ./*.mse-{style,game} %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-2
- Converted PKGBUILD to spec
