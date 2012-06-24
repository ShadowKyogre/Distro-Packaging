Name: mse-echo-magic-template
Version: 2.0.0
Release: 4%{?dist}
Summary: Custom Magic: the Gathering template by Echo and Blau
License: GPL
URL: http://magicseteditor.sourceforge.net/additional-templates
Source0: magic-echotemplate.zip::http://mtg.pifro.com/download/file.php?id=1718
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: mse-mtg ttf-gentium ttf-optimusprinceps
%description Custom Magic: the Gathering template by Echo and Blau

%prep
%setup -qn %_builddir/mse-echo-magic-template-2.0.0 -c %_builddir/mse-echo-magic-template-2.0.0

%build

    cd %_builddir;
    mkdir -p %_buildrootdir/usr/share/{magicseteditor/data,fonts/TTF};
    bsdtar -xf magic-echotemplate.mse-installer;
    chmod -x ./*.mse-style/*;
    cp -r ./*.mse-style %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-4
- Converted PKGBUILD to spec
