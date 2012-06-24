Name: ttf-masterforce-solid
Version: 1.0
Release: 1%{?dist}
Summary: Masterforce Solid font
License: freeware
URL: http://www.allfreefonts.com/font-4313-masterforce_solid.html
Source0: http://www.allfreefonts.com/download-4313-masterforce_solid-font.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: unzip
Requires: fontconfig xorg-font-utils
%description Masterforce Solid font

%prep
%setup -qn %_builddir/ttf-masterforce-solid-1.0 -c %_builddir/ttf-masterforce-solid-1.0

%build

    cd %_builddir;
    mkdir -p %_buildrootdir/usr/share/fonts/TTF;
    chmod -x ./*.TTF;
    cp -r ./*.TTF %_buildrootdir/usr/share/fonts/TTF

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
