Name: qtarot-git
Version: 20120619
Release: 1%{?dist}
Summary: A simple tarot reading program
License: GPL
URL: http://github.com/ShadowKyogre/QTarot/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: pyqt python-lxml
%description A simple tarot reading program

%prep
%setup -qn %_builddir/qtarot-git-20120619 -c %_builddir/qtarot-git-20120619

%build

    cd "%_builddir";
    if test -d "${_gitname}"; then
        cd "${_gitname}";
        git pull;
    else
        git clone "$_gitroot" "$_gitname" --depth=1;
    fi

%install

    cd "%_builddir/QTarot";
    mkdir -p %_buildrootdir/usr/{bin,share/{applications,qtarot,icons}};
    mkdir -p %_buildrootdir/usr/{bin,share/qtarot};
    cp -v *.py %_buildrootdir/usr/share/qtarot;
    cp QTarot.desktop %_buildrootdir/usr/share/applications/QTarot.desktop;
    cp qtarot.sh %_buildrootdir/usr/bin/qtarot;
    cp -Rv decks %_buildrootdir/usr/share/qtarot;
    cp -Rv deck_defs %_buildrootdir/usr/share/qtarot;
    cp -Rv layouts %_buildrootdir/usr/share/qtarot;
    cp -Rv hicolor %_buildrootdir/usr/share/icons;
    cp -v *.{xsd,html} %_buildrootdir/usr/share/qtarot

%files
%defattr(-,root,root,-)
/

%posttrans

    cat  <<-EndOfMessage
If you installed this program before 2/8/2012, you will need to do the following:
Edit ~/.config/ShadowKyogre/QTarot.ini and insert "deck=Rider Waite" into the "Reading" section
Then change the deck entry in the "Appearance" section to be skin=coleman-white.

EndOfMessage

    /bin/true

%post

    posttrans

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 20120619-1
- Converted PKGBUILD to spec
