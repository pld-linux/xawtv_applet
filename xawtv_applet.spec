Summary:	xawtv gnome-panel aplet
Name:		xawtv_applet
Version:	0.9.13
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://people.debian.org/~mvo/xawtv_applet/%{name}-%{version}.tar.gz
URL:		http://people.debian.org/~mvo/xawtv_applet/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xawtv_applet is a remote control for xawtv that runs inside the
gnome-panel.

%prep
%setup -q

%build
rm -f missing
aclocal -I macros
autoconf
automake -a -c -f
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README THANKS

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/vigor
