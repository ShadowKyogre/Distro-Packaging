Name: mse-vs
Version: 2.0.0
Release: 6%{?dist}
Summary: VS templates for Magic Set Editor.
License: freeware
URL: http://magicseteditor.sourceforge.net
Source0: http://downloads.sourceforge.net/magicseteditor/mse-linux32-2011-02-05-full.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: magicseteditor
%description VS templates for Magic Set Editor.

%prep
%setup -qn %_builddir/mse-vs-2.0.0 -c %_builddir/mse-vs-2.0.0

%build

    cd %_builddir;
    mkdir -p %_buildrootdir/usr/share/magicseteditor/data;
    cp -r ./magicseteditor/program/data/vs* %_buildrootdir/usr/share/magicseteditor/data

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-6
- Converted PKGBUILD to spec
