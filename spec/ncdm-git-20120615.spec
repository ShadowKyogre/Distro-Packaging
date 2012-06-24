Name: ncdm-git
Version: 20120615
Release: 6%{?dist}
Summary: An NCurses display manager
License: GPL
URL: https://github.com/ShadowKyogre/NCDM
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: python-urwid xorg-sessreg xorg-xinit coreutils kbd grep
%description An NCurses display manager

%prep
%setup -qn %_builddir/ncdm-git-20120615 -c %_builddir/ncdm-git-20120615

%build

    cd "%_builddir";
    if test -d NCDM; then
        cd NCDM;
        git pull;
    else
        git clone ${_gitroot} --depth=1;
    fi

%install

    cd "%_builddir/NCDM";
    mkdir -vp %_buildrootdir/usr/{share/ncdm{,/themes},bin};
    mkdir -vp %_buildrootdir/etc/ncdm;
    cp -v fbterm-bi ncdm %_buildrootdir/usr/bin;
    cp -v *.py %_buildrootdir/usr/share/ncdm;
    cp -v sys.cfg %_buildrootdir/etc/ncdm;
    cp -v default.json %_buildrootdir/usr/share/ncdm/themes

%files
%defattr(-,root,root,-)
/

%posttrans

    cat  <<-EndOfMessage

Warning, the following is alpha software. Please keep some
default tty lines so you don't lock yourself out of your system
if something goes awry.

Before you use NCDM, you should edit the following values to use
paths to files that actually exist:
THEME=./default.json
FBIMG=/path/to/image.ext

Suggested values:
THEME=/usr/share/ncdm/themes/default.json
FBIMAGE=/usr/share/wallpapers/<somethinghere.ext>

You should also create a cli.csv file with some sessions like this:
"Name","Command"
"TMUX","tmux"
"Login shell",""

More documentation for configuration can be found in /etc/ncdm/sys.cfg.

You can start up ncdm on a tty when the system starts by changing one of
your lines in /etc/inittab to look like this:
c1:12345:respawn:/usr/bin/ncdm tty1 linux

The default theme is also purposely gaudy so you can see
which properties in the default theme modify which parts of the UI.
EndOfMessage

    /bin/true

%post

    posttrans

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 20120615-6
- Converted PKGBUILD to spec
