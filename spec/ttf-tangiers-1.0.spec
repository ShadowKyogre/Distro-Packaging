Name: ttf-tangiers
Version: 1.0
Release: 1%{?dist}
Summary: A free alternative to the Algerian font
License: freeware
URL: http://www.fontsner.com/font/Tangiers_Normal-32393.html
Source0: Tangiers_Normal.ttf::http://www.fontsner.com/download/32393
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: fontconfig xorg-font-utils
%description A free alternative to the Algerian font

%prep
%setup -qn %_builddir/ttf-tangiers-1.0 -c %_builddir/ttf-tangiers-1.0

%build

    cd %_builddir;
    mkdir -p %_buildrootdir/usr/share/fonts/TTF;
    chmod -x ./*.ttf;
    cp -Lr ./*.ttf %_buildrootdir/usr/share/fonts/TTF

%files
%defattr(-,root,root,-)
/

%posttrans

    echo -n "Updating font cache... ";
    fc-cache -f > /dev/null;
    mkfontscale /usr/share/fonts/TTF;
    mkfontdir /usr/share/fonts/TTF;
    echo "done."

%post

    posttrans $1

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 1.0-1
- Converted PKGBUILD to spec
