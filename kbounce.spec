Name:		kbounce
Version:	15.08.1
Release:	1
Epoch:		1
Summary:	Claim areas and don't get disturbed
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://www.kde.org/applications/games/kbounce
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NotifyConfig)

%description
KBounce is a single player arcade game with the elements of puzzle.

It is played on a field, surrounded by wall, with two or more balls
bouncing around within the walls. The object of the game is to build
new walls to decrease the size of the active field.

%files
%doc %{_docdir}/*/*/kbounce
%{_bindir}/kbounce
%{_datadir}/applications/org.kde.kbounce.desktop
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

