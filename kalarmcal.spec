%define major 5
%define libname %mklibname KF5AlarmCal %{major}
%define devname %mklibname KF5AlarmCal -d

Name: kalarmcal
Version:	15.12.0
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	2
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary: Calendar support library for KAlarm
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(PythonInterp)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5Akonadi)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5IdentityManagement)
BuildRequires: cmake(KF5Holidays)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(KF5Holidays)

%description
Calendar support library for KAlarm.

%package -n %{libname}
Summary: Calendar support library for KAlarm
Group: System/Libraries

%description -n %{libname}
Calendar support library for KAlarm

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/*.so.4*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
