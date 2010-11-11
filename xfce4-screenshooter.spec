Summary:	Screenshooter application and plugin for Xfce panel
Summary(pl.UTF-8):	Aplikacja screenshooter i wtyczka dla panelu Xfce
Name:		xfce4-screenshooter
Version:	1.7.9
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/xfce4-screenshooter/1.7/%{name}-%{version}.tar.bz2
# Source0-md5:	c01d1cf3830bf8d60e09c0cdd223034c
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-screenshooter-plugin
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Obsoletes:	xfce4-screenshooter-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This application allows you to capture the entire screen, the active
window or a selected region. You can set the delay that elapses
before the screenshot is taken and the action that will be done with
the screenshot: save it to a PNG file, copy it to the clipboard, open
it using another application, or host it on ZimageZ, a free online
image hosting service.

A plugin for the Xfce panel is also available.

%description -l pl.UTF-8
Ta aplikacja umożliwia zrobienie zrzutu ekranu, aktywnego okna
albo zaznaczonego obszaru. Można ustawić opóźnienie przed zrobieniem
zrzutu ekranu i akcję, która zostanie wykonana po: zapisać do pliku
PNG, przenieść do schowka, otworzyć przy pomocy innego programu lub
umieścić na ZimageZ, darmowym serwisie hostowania obrazów.

Dostępna jest też wtyczka dla panelu Xfce.

%prep
%setup -q

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/xfce4-screenshooter
%{_datadir}/xfce4/panel-plugins/screenshooter.desktop
%{_desktopdir}/xfce4-screenshooter.desktop
%{_iconsdir}/hicolor/*/apps/applets-screenshooter.*
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-screenshooter-plugin
%{_mandir}/man1/xfce4-screenshooter.1.gz
%{_datadir}/xfce4/doc/C/*
%lang(ast) %{_datadir}/xfce4/doc/ast/*
%lang(ca) %{_datadir}/xfce4/doc/ca/*
%lang(da) %{_datadir}/xfce4/doc/da/*
%lang(es) %{_datadir}/xfce4/doc/es/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*
%lang(gl) %{_datadir}/xfce4/doc/gl/*
%lang(id) %{_datadir}/xfce4/doc/id/*
%lang(it) %{_datadir}/xfce4/doc/it/*
%lang(ja) %{_datadir}/xfce4/doc/ja/*
%lang(pt) %{_datadir}/xfce4/doc/pt/*
%lang(tr) %{_datadir}/xfce4/doc/tr/*
%lang(zh_CN) %{_datadir}/xfce4/doc/zh_CN/*
