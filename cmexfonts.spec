%define	fontdir	%{_datadir}/fonts/cmexfonts

Summary: CMEX chinese BDF fonts
Name: cmexfonts
Version: 0.2
Release: 1
License: MIT
Group: User Interface/X
URL: www.cmex.org.tw
BuildArch: noarch
Source0: %{name}-%{version}.zip
BuildRequires: xorg-x11-font-utils
Requires: fontconfig

%description
This package contains the standard Big5+ Chinese Ming 24x24 bitmap font (and
a resized 16x16 bitmap font) by CMEX and DynaLab for the X Window System
(PCF). This is one of the few Big5 or Big5+ Chinese bitmap fonts on the
Internet that is DFSG-compliant.

The font was designed by DynaLab and released by CMEX as part of the
proposed Big5+ standard documentation. It was then converted to HBF and BDF
format and further modified by Wei-Lun Chao in September 1998.

%prep
%setup -q -c

%build
bdftopcf cmex16m.bdf | gzip -c > cmex16m.pcf.gz
bdftopcf cmex24m.bdf | gzip -c > cmex24m.pcf.gz

%install
%__install -d $RPM_BUILD_ROOT%{fontdir}
%__install -m644 cmex16m.pcf.gz $RPM_BUILD_ROOT%{fontdir}
%__install -m644 cmex24m.pcf.gz $RPM_BUILD_ROOT%{fontdir}
mkfontdir $RPM_BUILD_ROOT%{fontdir}
install -d $RPM_BUILD_ROOT/etc/X11/fontpath.d
ln -s %{fontdir} $RPM_BUILD_ROOT/etc/X11/fontpath.d/%{name}

%post
fc-cache 2> /dev/null

%postun
fc-cache 2> /dev/null

%files
%{fontdir}
/etc/X11/fontpath.d/%{name}

%changelog
* Mon Feb 10 2014 Wei-Lun Chao <bluebat@member.fsf.org> 0.2-1
- initial package
