Name: ttf-dasroy
Version: 1.0
Release: 1%{?dist}
Summary: A titling font by Fabio Corubolo
License: freeware
URL: http://www.fontineed.com/font/DasRoy_Small_Caps
Source0: http://www.fontineed.com/downloads/DasRoy_Small_Caps.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: unzip
Requires: fontconfig xorg-font-utils
%description A titling font by Fabio Corubolo

%prep
%setup -qn %_builddir/ttf-dasroy-1.0 -c %_builddir/ttf-dasroy-1.0

%build

    cd %_builddir;
    unzip ${noextract[0]};
    mkdir -p %_buildrootdir/usr/share/fonts/TTF;
    chmod -x ./*.ttf;
    cp -r ./*.ttf %_buildrootdir/usr/share/fonts/TTF

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
