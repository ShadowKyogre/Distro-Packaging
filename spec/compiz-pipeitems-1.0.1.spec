Name: compiz-pipeitems
Version: 1.0.1
Release: 1%{?dist}
Summary: Compiz boxmenu pipeitems, most converted from some openbox pipemenus
License: GPL
URL: http://sourceforge.net/projects/compizboxmenupi
Source0: http://master.dl.sourceforge.net/project/compizboxmenupi/tarballs/compiz-boxmenu-pipeitems_-_1.0.1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: python2 bash
%description Compiz boxmenu pipeitems, most converted from some openbox pipemenus

%prep
%setup -qn %_builddir/compiz-pipeitems-1.0.1 -c %_builddir/compiz-pipeitems-1.0.1

%build

    mkdir -p %_buildrootdir/usr{/bin,/share/doc/compiz-pipes};
    msg "Putting pipeitems in correct location";
    cp -v %_builddir/compiz_pipes/cpz{audacious,bookmarks{,_icons},trash{,_icons},calendar{,_icons}.sh,places{,_icons}.sh,browse,filebrowser,weather.py} %_buildrootdir/usr/bin;
    cp -v %_builddir/compiz_pipes/manage_menus.sh %_buildrootdir/usr/bin;
    msg "Putting README in the correct location";
    cp -v %_builddir/compiz_pipes/README %_buildrootdir/usr/share/doc/compiz-pipes

%files
%defattr(-,root,root,-)
/

%posttrans

    cat  <<-EndOfMessage
==> How to use a pipeitem:
Insert <item type="launcher><command mode2="pipe">/path/to/the/script.extifany</command></item> into your menu via
a text editor. You can also add this by opening the editor, select
New, then click on pipeitem. Then type in the command for your pipeitem.
Be sure to also read the README in /usr/share/docs/compiz-pipes/README!
EndOfMessage

    /bin/true

%post

    posttrans

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 1.0.1-1
- Converted PKGBUILD to spec
