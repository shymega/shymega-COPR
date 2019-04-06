Name:           autocutsel
Version:        0.10.0
Release:        1%{?dist}
Summary:        Synchronizes the two copy/paste buffers mainly used by X applications.

License:        GPLv2
URL:            https://www.nongnu.org/%{name}
Source0:        https://github.com/sigmike/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  glibc-devel libXtst-devel libXaw-devel gcc gcc-c++


%description
Autocutsel tracks changes in the server's cutbuffer and CLIPBOARD
selection. When the CLIPBOARD is changed, it updates the
cutbuffer. When the cutbuffer is changed, it owns the CLIPBOARD
selection. The cutbuffer and CLIPBOARD selection are always
synchronized.

%prep
%autosetup


%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/autocutsel
%{_bindir}/cutsel

%license COPYING
%doc AUTHORS ChangeLog COPYING NEWS README TODO

%changelog
* Sun Sep 30 2018 Dom Rodriguez <shymega@shymega.org.uk> - Initial commit.
- Inital version of the RPM spec for maim.
