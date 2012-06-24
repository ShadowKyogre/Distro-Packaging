Name: magicseteditor
Version: 2.0.0
Release: 8%{?dist}
Summary: A program to help create Magic: the Gathering cards and sets. Comes with no game support.
License: GPL
URL: http://magicseteditor.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: boost unzip
Requires: hunspell libjpeg wxgtk boost-libs
%description A program to help create Magic: the Gathering cards and sets. Comes with no game support.

%prep
%setup -qn %_builddir/magicseteditor-2.0.0 -c %_builddir/magicseteditor-2.0.0

%build

    cd %_builddir;
    wget http://magicseteditor.svn.sourceforge.net/viewvc/magicseteditor/tags/releases/mse-${pkgver}/?view=tar -O magicseteditor-mse-${pkgver}.tar.gz;
    bsdtar -xf magicseteditor-mse-${pkgver}.tar.gz;
    cd ./mse-${pkgver};
    ./configure --prefix=/usr;
    sed -e 's|^\(AM_LDFLAGS = .*\),--as-needed|\1,-Bsymbolic-functions|' -i Makefile;
    make LIBS=-lhunspell-1.3 CPPFLAGS="-I/usr/include/hunspell -fpermissive" || return 1

%install

    cd ./mse-${pkgver};
    make DESTDIR=%_buildrootdir install || return 1;
    mkdir -p %_buildrootdir/usr/share/magicseteditor/{resource,data};
    cp -r ./data/*.mse-locale %_buildrootdir/usr/share/magicseteditor/data;
    cp -r ./src/resource/common/* %_buildrootdir/usr/share/magicseteditor/resource;
    cp -r ./src/resource/msw/other/* %_buildrootdir/usr/share/magicseteditor/resource;
    cp -r ./src/resource/msw/{cursor,icon,tool} %_buildrootdir/usr/share/magicseteditor/resource;
    rm -rf %_buildrootdir/usr/share/magicseteditor/resource/{cursor,icon,tool}/.svn;
    rm -rf %_buildrootdir/usr/share/magicseteditor/data/.svn;
    rm -rf %_buildrootdir/usr/share/magicseteditor/data/*/.svn

%files
%defattr(-,root,root,-)
/

%posttrans

    cat  <<-EndOfMessage
The fonts required for this package can't be put on the AUR due to licensing issues.
In order to get them, download the binary release here:
http://downloads.sourceforge.net/magicseteditor/mse-linux32-2011-02-05-full.tar.gz
Copy the fonts into your /usr/share/fonts/TTF folder or wrap them up
with some fancy PKGBUILD of your own.

You may also want to install one or more of the following packages:
mse-ygo or mse-ygo-xyz for YuGiOh! support
mse-mtg or mse-mtg-phyrexian for Magic: the Gathering support
mse-vs for VS support

Happy editing!
EndOfMessage

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 2.0.0-8
- Converted PKGBUILD to spec
