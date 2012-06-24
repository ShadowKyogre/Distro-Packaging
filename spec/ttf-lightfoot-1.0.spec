Name: ttf-lightfoot
Version: 1.0
Release: 1%{?dist}
Summary: Lightfoot font by Paul Lloyd
License: freeware
URL: http://www.fontstock.net/type-designers/paul-lloyd.html
Source0: Lightfoot.zip::http://www.fontstock.net/download/download.ashx?d=317207
Source1: Lightfoot-Narrow-Extra-condensed-Regular.zip::http://www.fontstock.net/download/download.ashx?d=317211
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: fontconfig xorg-font-utils
%description Lightfoot font by Paul Lloyd

%prep
%setup -qn %_builddir/ttf-lightfoot-1.0 -c %_builddir/ttf-lightfoot-1.0

%build

    mkdir -p %_buildrootdir/usr/share/fonts/TTF;
    cd %_builddir;
    cp -r ./*/*.ttf %_buildrootdir/usr/share/fonts/TTF/

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 1.0-1
- Converted PKGBUILD to spec
