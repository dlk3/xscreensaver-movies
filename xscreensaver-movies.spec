Name:           xscreensaver-movies
Version:        0.3
Release:        1%{?dist}
Summary:        Play videos as xscreensaver screen savers

License:        MIT
URL:            https://github.com/dlk3/xscreensaver-movies
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       xscreensaver-base
Requires:       mpv

%description
This is a Python script that will play video files as screen savers in
xscreensaver. The video files are played in random order and do not
repeat until all files have been played.


%prep
%autosetup


%install
mkdir -p %{buildroot}/usr/libexec/xscreensaver/
install -m 755 xscreensaver-movies %{buildroot}/usr/libexec/xscreensaver/xscreensaver-movies
mkdir -p %{buildroot}/usr/share/xscreensaver/hacks.conf.d/
install -m 644 xscreensaver-movies.conf %{buildroot}/usr/share/xscreensaver/hacks.conf.d/xscreensaver-movies.conf
mkdir -p %{buildroot}/usr/share/xscreensaver/config/
install -m 644 xscreensaver-movies.xml %{buildroot}/usr/share/xscreensaver/config/xscreensaver-movies.xml


%files
%license LICENSE
%doc README.md
/usr/libexec/xscreensaver/xscreensaver-movies
/usr/share/xscreensaver/hacks.conf.d/xscreensaver-movies.conf
/usr/share/xscreensaver/config/xscreensaver-movies.xml


%post
%{_sbindir}/update-xscreensaver-hacks


%changelog
* Sun Dec 15 2019 David King <dave@daveking.com>
- Add --hwdec=auto option to mpv command
* Sun Dec  1 2019 David King <dave@daveking.com>
- Initial release
