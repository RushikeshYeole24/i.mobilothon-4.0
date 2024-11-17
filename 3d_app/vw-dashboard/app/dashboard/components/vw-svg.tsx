const VWID4SVG = () => (
    <svg viewBox="0 0 1200 500" className="w-full h-full">
      <defs>
        {/* Body Gradient */}
        <linearGradient id="carBody" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" style={{ stopColor: '#4a4a4a', stopOpacity: 1 }} />
          <stop offset="50%" style={{ stopColor: '#606060', stopOpacity: 1 }} />
          <stop offset="100%" style={{ stopColor: '#4a4a4a', stopOpacity: 1 }} />
        </linearGradient>
        
        {/* Window Gradient */}
        <linearGradient id="windowGlass" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" style={{ stopColor: '#a8d8ff', stopOpacity: 0.7 }} />
          <stop offset="100%" style={{ stopColor: '#6ca0dc', stopOpacity: 0.9 }} />
        </linearGradient>
  
        {/* Wheel Gradient */}
        <radialGradient id="wheelDetail" cx="50%" cy="50%" r="50%">
          <stop offset="70%" style={{ stopColor: '#333' }} />
          <stop offset="100%" style={{ stopColor: '#1a1a1a' }} />
        </radialGradient>
      </defs>
  
      <g transform="translate(150, 100)">
        {/* Car Body */}
        <path
          d="M100,250 C100,200 150,150 250,150 
             L700,150 C800,150 850,200 850,250 
             L860,300 C860,330 840,350 800,350 
             L150,350 C120,350 100,330 100,300 Z"
          fill="url(#carBody)"
          stroke="#222"
          strokeWidth="2"
        />
  
        {/* Roof */}
        <path
          d="M250,150 C270,100 680,100 700,150"
          fill="url(#carBody)"
          stroke="#222"
          strokeWidth="2"
        />
  
        {/* Windshield */}
        <path
          d="M250,150 C270,120 680,120 700,150"
          fill="url(#windowGlass)"
          stroke="#333"
          strokeWidth="1.5"
        />
  
        {/* Side Windows */}
        <path
          d="M720,150 C740,120 830,120 850,150"
          fill="url(#windowGlass)"
          stroke="#333"
          strokeWidth="1.5"
        />
  
        {/* Headlights */}
        <circle cx="130" cy="250" r="15" fill="#FFF" />
        <circle cx="130" cy="250" r="10" fill="#FFD700" opacity="0.8" />
        
        {/* Tail Lights */}
        <rect x="820" y="240" width="20" height="30" fill="#FF0000" opacity="0.9" />
  
        {/* Wheels */}
        {[
          { cx: 250, cy: 350 },
          { cx: 700, cy: 350 },
        ].map(({ cx, cy }, index) => (
          <g key={index} transform={`translate(${cx}, ${cy})`}>
            <circle cx="0" cy="0" r="45" fill="#1a1a1a" />
            <circle cx="0" cy="0" r="35" fill="url(#wheelDetail)" />
            <circle cx="0" cy="0" r="25" fill="#444" />
            {[...Array(8)].map((_, i) => (
              <rect
                key={i}
                x="-2"
                y="-25"
                width="4"
                height="50"
                fill="#666"
                transform={`rotate(${i * 45})`}
              />
            ))}
          </g>
        ))}
  
        {/* Ground Shadow */}
        <ellipse
          cx="475"
          cy="420"
          rx="400"
          ry="30"
          fill="#000"
          opacity="0.2"
        />
      </g>
    </svg>
  );
  
  export default VWID4SVG;
  