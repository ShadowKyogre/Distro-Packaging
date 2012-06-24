Name: ttf-optimusprinceps
Version: 1.0
Release: 1%{?dist}
Summary: Optimus Princeps font by Manfred Klein
License: freeware
URL: http://www.dafont.com/optimusprinceps.font
Source0: optimusprinceps.zip::http://img.dafont.com/dl/?f=optimusprinceps
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: unzip
Requires: fontconfig xorg-font-utils
%description Optimus Princeps font by Manfred Klein

%prep
%setup -qn %_builddir/ttf-optimusprinceps-1.0 -c %_builddir/ttf-optimusprinceps-1.0

%build

    cd %_builddir;
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
