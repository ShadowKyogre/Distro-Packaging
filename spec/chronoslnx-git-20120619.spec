Name: chronoslnx-git
Version: 20120619
Release: 1%{?dist}
Summary: A planetary hours/aspect overview program
License: GPL
URL: http://shadowkyogre.github.com/ChronosLNX/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: git
Requires: pyqt python-dateutil pyswisseph3 swisseph_18
%description A planetary hours/aspect overview program

%prep
%setup -qn %_builddir/chronoslnx-git-20120619 -c %_builddir/chronoslnx-git-20120619

%build

    cd "%_builddir";
    if test -d "${_gitname}"; then
        cd "${_gitname}";
        git pull;
    else
        git clone "$_gitroot" "$_gitname" --depth=1;
    fi

%install

    cd "%_builddir/ChronosLNX";
    mkdir -p %_buildrootdir/usr/{bin,share/{applications,chronoslnx}};
    cp -v *.py %_buildrootdir/usr/share/chronoslnx;
    cp -v ChronosLNX.desktop %_buildrootdir/usr/share/applications;
    cp -v chronoslnx.sh %_buildrootdir/usr/bin/chronoslnx;
    cp -v schedule.csv %_buildrootdir/usr/share/chronoslnx;
    cp -vR themes %_buildrootdir/usr/share/chronoslnx

%files
%defattr(-,root,root,-)
/

%posttrans

    cat  <<-EndOfMessage
If you were running a previous version of this, you WILL need to backup 
your configuration. The PyQt for python2 and python3 are not compatible.
______
Don't like the current logo? You can disable it or change it by doing the following

mkdir -p ~/.local/share/data/ChronosLNX/themes/DarkGlyphs/misc/

touch ~/.local/share/data/ChronosLNX/themes/DarkGlyphs/misc/chronoslnx.png
OR
Use an image editor to make another icon in this location.

You can override any icon in a theme by doing this.

EndOfMessage

    /bin/true

%post

    posttrans

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 20120619-1
- Converted PKGBUILD to spec
