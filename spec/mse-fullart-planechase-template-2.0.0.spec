Name: mse-fullart-planechase-template
Version: 2.0.0
Release: 3%{?dist}
Summary: A horizontal fullart plane style for Magic: the Gathering plane cards
License: GPL
URL: http://magicseteditor.sourceforge.net/additional-templates
Source0: planechase-fullart-horizontal.mse-installer::http://mtg.pifro.com/download/file.php?id=2195&sid=464e2430d4602a0d36062f206b3e3a5e
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: mse-mtg
%description A horizontal fullart plane style for Magic: the Gathering plane cards

%prep
%setup -qn %_builddir/mse-fullart-planechase-template-2.0.0 -c %_builddir/mse-fullart-planechase-template-2.0.0

%build

    cd %_builddir;
    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    bsdtar -xf planechase-fullart-horizontal.mse-installer;
    chmod -x ./*.mse-style/*;
    cp -r ./*.mse-style %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-3
- Converted PKGBUILD to spec
