Name:		kbounce
Version:	4.10.3
Release:	1
Epoch:		1
Summary:	Claim areas and don't get disturbed
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kbounce
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
KBounce is a single player arcade game with the elements of puzzle.

It is played on a field, surrounded by wall, with two or more balls
bouncing around within the walls. The object of the game is to build
new walls to decrease the size of the active field.

%files
%{_kde_bindir}/kbounce
%{_kde_applicationsdir}/kbounce.desktop
%{_kde_appsdir}/kbounce
%{_kde_iconsdir}/*/*/apps/kbounce*
%{_kde_docdir}/*/*/kbounce

#-------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

