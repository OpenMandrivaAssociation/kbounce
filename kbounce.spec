Name:		kbounce
Version:	20.08.1
Release:	1
Epoch:		1
Summary:	Claim areas and don't get disturbed
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://www.kde.org/applications/games/kbounce
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5KDEGames)

%description
KBounce is a single player arcade game with the elements of puzzle.

It is played on a field, surrounded by wall, with two or more balls
bouncing around within the walls. The object of the game is to build
new walls to decrease the size of the active field.

%files -f %{name}.lang
%{_bindir}/kbounce
%{_datadir}/applications/org.kde.kbounce.desktop
%{_datadir}/metainfo/org.kde.kbounce.appdata.xml
%{_datadir}/kxmlgui5/kbounce/kbounceui.rc
%{_datadir}/kbounce
%{_iconsdir}/*/*/apps/kbounce*


#-------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
