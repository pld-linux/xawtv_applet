Summary:	xawtv gnome-panel aplet
Summary(pl):	Aplet panelu GNOME xawtv
Name:		xawtv_applet
Version:	0.9.13
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://people.debian.org/~mvo/xawtv_applet/%{name}-%{version}.tar.gz
# Source0-md5:	30890e275ee8a89638bdc076527e3339
URL:		http://people.debian.org/~mvo/xawtv_applet/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-core-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME

%description
xawtv_applet is a remote control for xawtv that runs inside the
gnome-panel.

%description -l pl
xawtv_applet to pilot dla xawtv dzia³aj±cy wewn±trz panelu GNOME.

%prep
%setup -q

%build
rm -f missing
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pixmapdir=%{_pixmapsdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/xawtv_applet
%{_sysconfdir}/CORBA/servers/xawtv_applet.gnorba
%{_datadir}/applets/Multimedia/*
%{_pixmapsdir}/*
