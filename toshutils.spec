Version: 	2.0.1
Summary: 	Toshiba laptop utilities
Name: 		toshutils
Release: 	%mkrel 3
License: 	GPL
Group: 		Monitoring
Source: 	http://www.buzzard.me.uk/toshiba/%{name}-%{version}.tar.bz2
Patch0:		toshutils-2.0.1-module.patch.bz2
Patch1:		toshutils-2.0.1-devfs.patch.bz2
Patch2:		toshutils-2.0.1-crash.patch.bz2
Patch3:		toshutils-2.0.1-x86_64-support.patch.bz2
Patch4:		toshutils-2.0.1-gcc4.patch.bz2
URL: 		http://www.buzzard.me.uk/toshiba/index.html
BuildRequires:	gtk+1.2-devel X11-devel yacc

%description
This is a collection of utilities to control a Toshiba laptop. It includes
programs to turn the fan on and off, to view the power mode, and to set the
supervisor password.

Note that these utilities work with APM features in the Toshiba BIOS. 
If your laptop's BIOS only supports ACPI and not APM, then toshutils will
probably not work for you. Toshiba's newer models tend to support ACPI
only, and therefore toshutils will not work with them.


%prep
%setup -q 
%patch0 -p0
%patch1 -p1
# workaround crash:
%patch2 -p1
%ifarch x86_64
%patch3 -p1
%endif
%patch4 -p1

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%_bindir,%_mandir/man{1,8}}
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README.* COPYING 
%_bindir/*
%_mandir/man?/*
