Name:           xscreensaver-movies
Version:        0.1
Release:        0.1%{?dist}
Summary:        Play videos as xscreensaver screensavers

License:        MIT
URL:            https://github.com/dlk3/xscreensaver-movies
Source0:        xscreensaver-movies-0.1.tar.gz
BuildArch:      noarch

Requires:       xscreensaver-base
Requires:       mpv

%description
This is a Python script that will play video files as screensavers in xscreensaver. The video files are played in random order and do not repeat until all files have been played.


%prep
%autosetup


%build


%install
mkdir -p %{buildroot}/usr/libexec/xscreensaver/
install -m 755 xscreensaver-movies %{buildroot}/usr/libexec/xscreensaver/xscreensaver-movies
mkdir -p %{buildroot}/usr/share/xscreensaver/hacks.conf.d/
install -m 755 xscreensaver-movies.conf %{buildroot}/usr/share/xscreensaver/hacks.conf.d/xscreensaver-movies.conf


%files
%license LICENSE
%doc README.md
/usr/libexec/xscreensaver/xscreensaver-movies
/usr/share/xscreensaver/hacks.conf.d/xscreensaver-movies.conf


%post
%{_sbindir}/update-xscreensaver-hacks


%changelog
* Sun Dec  1 2019 David King <dave@daveking.com>
- 
