#
%define		_state		stable
%define		orgname		plasmate
%define		qtver		4.8.1

Summary:	K Desktop Environment - IDE tailored for development of Plasma components
Name:		kde4-plasmate
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/plasmate/%{version}/src/%{orgname}-%{version}.tar.gz
# Source0-md5:	342e5cdc36e4e1a524b258ca32f1acad
URL:		http://www.kde.org/
BuildRequires:	QtWebKit-devel
BuildRequires:	attica-devel
BuildRequires:	git-core
BuildRequires:	gpgme-devel
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	soprano-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small IDE tailored for development of Plasma components, such as
Widgets, Runners, Dataengines.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwin-windowswitcherpreviewer
%attr(755,root,root) %{_bindir}/plasma-remote-widgets-browser
%attr(755,root,root) %{_bindir}/plasmaengineexplorer
%attr(755,root,root) %{_bindir}/plasmakconfigxteditor
%attr(755,root,root) %{_bindir}/plasmaremoteinstaller
%attr(755,root,root) %{_bindir}/plasmate
%attr(755,root,root) %{_bindir}/plasmawallpaperviewer
%attr(755,root,root) %{_bindir}/plasmoidviewer
%attr(755,root,root) %{_libdir}/kde4/plasma_containment_studiopreviewer.so
%{_desktopdir}/kde4/plasmate.desktop
%{_datadir}/apps/plasmate
%{_datadir}/config/plasmate.knsrc
%{_datadir}/kde4/services/plasma-containment-studiopreviewer.desktop
%{_iconsdir}/hicolor/*x*/apps/plasmagik.png
%{_mandir}/man1/plasmaengineexplorer.1*
%{_mandir}/man1/plasmoidviewer.1*
