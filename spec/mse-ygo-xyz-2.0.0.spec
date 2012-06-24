Name: mse-ygo-xyz
Version: 2.0.0
Release: 6%{?dist}
Summary: YugiOh template with xyz additions for Magic Set Editor.
License: freeware
URL: http://forum.yugiohcardmaker.net/topic/240063-mse-xyz-monsters-v5-now-you-can-make-your-own/
Source0: http://dl.dropbox.com/u/12096853/XyzV5.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: unzip
Requires: magicseteditor
%description YugiOh template with xyz additions for Magic Set Editor.

%prep
%setup -qn %_builddir/mse-ygo-xyz-2.0.0 -c %_builddir/mse-ygo-xyz-2.0.0

%build

    cd %_builddir;
    unzip XyzV5.zip;
    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    rm -vf ./data/*.mse-symbol-font/build.bat;
    cp -r ./data/*.mse-{symbol-font,game,style} %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-6
- Converted PKGBUILD to spec
